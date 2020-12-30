$(document).ready(function() {
    $("#magnify").click(function() {
      $(".search").toggleClass("focus");
      $("#magnify").toggleClass("clicked");
    });
});