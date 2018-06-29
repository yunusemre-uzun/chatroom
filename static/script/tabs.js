//TODO pressing enter intead of clickinng send button in tabs leads to error
//TODO add friend has a little visual bug
//TODO mesages does not scroll to bottom when the page is opened

$( function() {
    var tabTitle = $( "#tab_title" ),
      tabTemplate = "<li><a href='#{href}'>#{label}</a> <span class='ui-icon ui-icon-close' role='presentation'>Remove Tab</span></li>",
      tabCounter = 2;

    var tabs = $( "#tabs" ).tabs();

    // Modal dialog init: custom buttons and a "close" callback resetting the form inside
    var dialog = $( "#dialog" ).dialog({
      autoOpen: false,
      modal: true,
      buttons: {
        Add: function() {
          addTab();
          $( this ).dialog( "close" );
        },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
      },
      close: function() {
        form[ 0 ].reset();
      }
    });

    // AddTab form: calls addTab function on submit and closes the dialog
    var form = dialog.find( "form" ).on( "submit", function( event ) {
      addTab();
      dialog.dialog( "close" );
      event.preventDefault();
    });

    // Actual addTab function: adds new tab using the input from the form above
    function addTab() {
      var label = tabTitle.val() || "Tab " + tabCounter,
        id = "tabs-" + tabCounter,
        li = $( tabTemplate.replace( /#\{href\}/g, "#" + label ).replace( /#\{label\}/g, label ) ),
        tabContentHtml =  "";

        prevLabels =  Cookies.get('labels');
        if(typeof(prevLabels)!="undefined" && !prevLabels.includes(label) ){
            Cookies.set('labels',prevLabels + ":" + label,{path:"/"});
        }
        else if(typeof(prevLabels)!="undefined" && prevLabels.includes(label)){
            window.alert("This tab already exists");
            return;
        }
        else if(typeof(prevLabels)=="undefined"){
            Cookies.set('labels',label,{path:"/"});
        }
        location.reload();

    }

    // AddTab button: just opens the dialog
    $( "#add_tab" )
      .button()
      .on( "click", function() {
        dialog.dialog( "open" );
      });

    // Close icon: removing the tab on click
    tabs.on( "click", "span.ui-icon-close", function() {
      var panelId = $( this ).closest( "li" ).remove().attr( "aria-controls" ),
          currentTabId=$( "#" + panelId ).selector.slice(1);
        prevLabels =  Cookies.get('labels').split(":");
        tabIndex = prevLabels.indexOf(currentTabId);

        if (typeof(prevLabels)!="undefined" && tabIndex !== -1) {
            prevLabels = prevLabels.filter(function(item) {
                return item !== currentTabId;
            })


            if(prevLabels.length == 0){
                console.log('here', prevLabels);
                Cookies.remove('labels', { path: '/' });

            }
            else{
                Cookies.set('labels',prevLabels, {path:'/'});
            }
        }

      $( "#" + panelId ).remove();
      //location.reload();

    });

    tabs.on( "keyup", function( event ) {
      if ( event.altKey && event.keyCode === $.ui.keyCode.BACKSPACE ) {
        var panelId = tabs.find( ".ui-tabs-active" ).remove().attr( "aria-controls" );
        $( "#" + panelId ).remove();
        tabs.tabs( "refresh" );
      }
    });

    function addCookieTab() {
        var labels = Cookies.get('labels'),
            id = "tabs-" + tabCounter;
        var labelList,
         tabContentHtml =  "";


        if (typeof(labels) != "undefined") {
            labelList = labels.split(":");
            for (i = 0; i < labelList.length; i++) {
                id = "tabs-" + tabCounter;
                li = $( tabTemplate.replace( /#\{href\}/g, "#" + labelList[i] ).replace( /#\{label\}/g, labelList[i] ) );


                for( j = 0 ; j<userMessagesArray.length ;j++){

                    if(String(userMessagesArray[j][0])=== String(labelList[i])){
                         tabContentHtml = " <div id = 'messages'>"+userMessagesArray[j].slice(1).join(" ")+"</div>";

                    }
                }

                //Creates a form that saves the message to database on click

                var f = document.createElement("form");
                f.setAttribute('method',"post");
                f.setAttribute('id',labelList[i]);
                f.setAttribute('name',labelList[i]);
                f.onclick = function onclick(event){
                    var message_text = String(document.getElementById("message_"+String(this.name)).value);
                    if(message_text !== ""){
                      $.ajax({
                        url: '/user/'+username+'/chat/'+this.name + '/' + message_text + '/' ,
                        dataType : 'html',
                        timeout : 30000,
                        success: function(data){
                            position_of_id_begin = data.search("<data>")+6;
                            position_of_id_end = data.search("</data>");
                            var id =  data.slice(position_of_id_begin,position_of_id_end)

                            $('input[type="text"]').val("");
                            $('#' + id + ' > #messages' ).append(data.slice(position_of_id_end+7));
                             $('#' + id + ' > #messages' ).scrollTop($('#' + id + ' > #messages' )[0].scrollHeight);
                            }
                    });

                   ;}

                };

                var k = document.createElement("input");
                k.setAttribute('type', 'text');
                k.setAttribute('name', labelList[i]);
                k.setAttribute('id', "message_"+labelList[i]);

                var s = document.createElement("input");
                s.type = "button";
                s.value = "Submit";
                s.setAttribute('id', "button_"+labelList[i]);



                f.appendChild(k);
                f.appendChild(s);

                var inputElem = document.createElement('input');
                inputElem.type = 'hidden';
                inputElem.name = 'csrfmiddlewaretoken';
                inputElem.value = Cookies.get('csrftoken');
                f.appendChild(inputElem);

                var cssText = "<style>#messages{\n" +
                    "\n" +
                    "    height: 600px;\n" +
                    "    padding: 15px;\n" +
                    "    margin: 25px;\n" +
                    "    left:100%;\n" +
                    "    overflow-y: scroll;\n" +
                    "    overflow-x: hidden;\n" +
                    "} </style>";
                tabs.find( ".ui-tabs-nav" ).append( li );
                tabs.append( cssText + "<div id='" + labelList[i] + "'><p>" + tabContentHtml + "</p></div>" );
                $('#' + labelList[i] + ' > #messages' ).scrollTop($('#' + labelList[i] + ' > #messages' )[0].scrollHeight)
                $('#'+labelList[i]).append(f);
                tabs.tabs( "refresh" );
                tabCounter++;
                id = "tabs-" + tabCounter;
                tabContentHtml =  "";
            }
        }
        $( "#tabs" ).tabs({ active: 0 });

    }
    $( document ).ready(function() {
        addCookieTab();
    });
  } );

function refreshTabs(new_data){
  var tabcont=document.getElementById("tabs")
  var tabs = tabcont.childNodes;
  var tab_count = tabs.length;
  if(new_data=="" || typeof(new_data)=="undefined"){
    return;
  }
  if(tab_count==1){
    return;
  }
  else{
    for(var i=1;i<tab_count;i++){
      var id = tabs[i].id;
      if(id=="" || typeof(id)=="undefined"){
        continue;
      }
      if(findMessages(id,new_data)==[]){
          continue;
      }
      $('#' + id + ' > #messages' ).append(findMessages(id,new_data))
      $('#' + id + ' > #messages' ).scrollTop($('#' + id + ' > #messages' )[0].scrollHeight)
    }
    return;
  }
}
function findMessages(id,data){
  ret = []
  data = data.slice(1,data.length-1);
  my_data = data.split("][");
  for(var i=0;i<my_data.length;i++){
    position_of_id_begin = my_data[i].search("<strong>")+8;
    position_of_id_end = my_data[i].search("</strong>");
    if(my_data[i].slice(position_of_id_begin,position_of_id_end)==id){
        p1 = my_data[i].search("<h4>");
        p2 = my_data[i].search("</h4>")+5;
        ret.push(my_data[i].slice(p1,p2));
    }
  }
  return ret;
}

function refreshtabs() {
  $.ajax({
      url: '/user/chatroom/'+username,
      dataType : 'html',
      timeout : 30000,
      success: function(data){
          refreshTabs(data)
          //$('#messageList').html(data);
      }
  });

}
setInterval(refreshtabs,3000);

function scrollToBottom (id) {
   var div = document.getElementById(id);
   div.scrollTop = div.scrollHeight - div.clientHeight;
}

