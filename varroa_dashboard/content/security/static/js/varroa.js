var securityRisks = (function() {

  var security = {};

  /* Public function to highlight a resource panel */
  security.showResourceRisks = function(pageHash) {
    var resourceId = pageHash.replace('#!','');
    console.log(resourceId);
    // Highlight the resource panel on page load
    $(resourceId + "_panel").removeClass("panel-default").addClass('panel-primary');
  };

  // Return public functions
  return security;
}());
