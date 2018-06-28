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
            Cookies.set('labels',prevLabels + ":" + label);
        }
        else if(typeof(prevLabels)!="undefined" && prevLabels.includes(label)){
            window.alert("This tab already exists");
            return;
        }
        else if(typeof(prevLabels)=="undefined"){
            Cookies.set('labels',label,{path:"/"});
        }

      tabs.find( ".ui-tabs-nav" ).append( li );
      tabs.append( "<div id='" + label + "'><p>" + tabContentHtml + "</p></div>" );
      tabs.tabs( "refresh" );
      tabCounter++;
       console.log(Cookies.get('labels'));
    }

    // AddTab button: just opens the dialog
    $( "#add_tab" )
      .button()
      .on( "click", function() {
        dialog.dialog( "open" );
      });

    // Close icon: removing the tab on click
    tabs.on( "click", "span.ui-icon-close", function() {
      var panelId = $( this ).closest( "li" ).remove().attr( "aria-controls" );
      $( "#" + panelId ).remove();
      tabs.tabs( "refresh" );
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
            console.log(labelList);
            for (i = 0; i < labelList.length; i++) {
                id = "tabs-" + tabCounter,
                    li = $( tabTemplate.replace( /#\{href\}/g, "#" + labelList[i] ).replace( /#\{label\}/g, labelList[i] ) ),
              tabs.find( ".ui-tabs-nav" ).append( li );
              tabs.append( "<div id='" + labelList[i] + "'><p>" + tabContentHtml + "</p></div>" );
              tabs.tabs( "refresh" );
              tabCounter++;
              id = "tabs-" + tabCounter;
            }
        }

    }
    $( document ).ready(function() {
        addCookieTab();
    });
  } );

function refreshTabs(new_data){
  var tabcont=document.getElementById("tabs")
  var tabs = tabcont.childNodes;
  var tab_count = tabs.length;
  if(new_data==""){
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
      elem=document.getElementById(id);
      prev_content=elem.innerText;
      content_to_be_added = findMessages(id,new_data);
      console.log(content_to_be_added);
      elem.innerHTML = prev_content + content_to_be_added;
      console.log(elem.innerText);
    }
    return;
  }
}
function findMessages(id,data){
  ret = []
  my_data = data.split("][");
  for(var i=0;i<my_data.length;i++){
    position_of_id_begin = my_data[i].search("<strong>")+8;
    position_of_id_end = my_data[i].search("</strong>");
    if(data.slice(position_of_id_begin,position_of_id_end)==id){
      ret.push(my_data[i].slice(1,(my_data[i].length)-1));
    }
  }
  return ret;
}

function refreshtabs() {
  //console.log("refreshtabs");
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
$( document ).ready(function() {
  // addCookieTab();
  refreshtabs();
});

