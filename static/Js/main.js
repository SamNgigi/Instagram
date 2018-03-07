$(document).ready(function() {
  console.log('working');
  // alert('Working')
    // $('.fa-heart').hide()
    $('.fa-heart').on('click', function(e) {
      e.preventDefault()
      var postId = $(this).attr('id').split('-')[1];
      console.log("clicked" + postId);
      // $(this).('.fa-heart-o, .fa-heart').toggle()
      $(this).toggleClass("red")
  })
});
