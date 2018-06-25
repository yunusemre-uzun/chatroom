console.log('open2');

function refresh() {
    console.log("refresh");
    $.ajax({
        url: '',
        dataType : 'html',
        timeout : 30000,
        success: function(data){
            $('#friends').html(data);
        }
    });
}
setTimeout(refresh,3000);
// When the user clicks on <div>, open the popup
function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("hide");
}
setTimeout(myFunction, 0);

// Script to open and close sidebar
function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
}

function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
}

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}
$( function() {
    var tabTitle = $( "#tab_title" ),
    tabContent = $("#tab_content"),
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
        li = $( tabTemplate.replace( /#\{href\}/g, "#" + id ).replace( /#\{label\}/g, label ) ),
        tabContentHtml = tabContent.val() || "Tab " + tabCounter + " content.";

    tabs.find( ".ui-tabs-nav" ).append( li );
    tabs.append( "<div id='" + id + "'><p>" + tabContentHtml + "</p></div>" );
    tabs.tabs( "refresh" );
    tabCounter++;
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
} );

