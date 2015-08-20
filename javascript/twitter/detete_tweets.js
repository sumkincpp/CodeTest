// Run in JS console from twitter.com/<yourusername>
// This will (duh) delete all your tweets. Don't be dumb
var deleteLoop;
deleteLoop = setInterval(function(){
  var deleteButton = $('.js-actionDelete button');
  if(deleteButton.length < 1){
    clearInterval(deleteLoop);
    alert('No more things to delete');
  } else {
    deleteButton[0].click();
    setTimeout(function(){
      $('.delete-action').click();
    }, 500);
  }
}, 1200);
// source: https://github.com/banterability/first-listen/blob/089447299162c23f9ce4a76ee449a9a0b60d9c9e/util/delete_all_tweets.js
