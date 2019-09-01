
// $('.grid').masonry({
//     itemSelector:'.grid-item',
//     columnWidth:160,
//     gutter:10
// })


// init Masonry after all images have loaded
var $grid = $('.grid').imagesLoaded( function() {
    $grid.masonry({
      itemSelector: '.grid-item',
      percentPosition: true,
      columnWidth: '.grid-sizer',
      gutter:10
    }); 
  });








