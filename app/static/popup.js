$(function(){
    $('.play').click(function(){ 
        console.log('clicked')
        console.log('here')
        $('#iframeHolder').html('<iframe id="iframe" src="{{ song[0] }} width="700" height="450"></iframe>');
    });   
});