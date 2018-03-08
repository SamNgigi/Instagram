$(document).ready(function() {
  console.log('working');
  // alert('Working')
  // $('.fa-heart').hide()
  var liked = true;
  heart = $('.fa-heart')
  count = parseInt($('.like-count').text())
  console.log(count);
  heart.on('click', function(e) {
    e.preventDefault()
    var postId = $(this).attr('data-post-id').split('-')[1];
    if (liked) {
      // var likeId = $(e.target).data('likeId')
      likes = count+1;
      // console.log(likes);
      // $(e.target).data('likeId').text(likes)
      $('.like-count').text(likes)
      // console.log('i like');
      liked = false
    } else if(!liked) {

      likes = likes-1;
      // console.log(likes);
      $('.like-count').text(likes)
      // console.log('weeeeeell');
      liked = true
    }
    // var like_count = 1
    // console.log("clicked" + postId + clicked);
    // $(this).('.fa-heart-o, .fa-heart').toggle()
    $(this).toggleClass("red")


    $.ajax({
      'url':'/ajax/likes/postId',
      'type': 'POST',
      "dataType": "json",
      'data':'likes',
      "success": function(data) {
          console.log(data);
      },
    });

  })
});
