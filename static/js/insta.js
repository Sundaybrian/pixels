// masonry
// $('.grid').masonry({
//     itemSelector:'.grid-item',
//     columnWidth:110,
//     fitWidth:true,
//     gutter:0
// })


// init Masonry after all images have loaded
var $grid = $('.grid').imagesLoaded( function() {
    $grid.masonry({
      itemSelector: '.grid-item',
      percentPosition: true,
      columnWidth: '.grid-sizer'
    }); 
  });








