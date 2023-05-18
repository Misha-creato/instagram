
$(document).ready(function(){
    $(".post-like").click(function(){
        let post_id = $(this).closest('.post')[0].id;
        let like = $(this)[0]
        let previous_status = 'fa-regular'
        let new_status = ''
        if (like.className.includes(previous_status)) {
            new_status = 'fa-solid'
        }
        else {
            previous_status = 'fa-solid'
            new_status = 'fa-regular'
        }
        console.log(previous_status, new_status)
        $.ajax
        ({
            url: `post_like/${post_id}/`,
            type: 'POST',
            success: function(result){
                like.classList.replace(previous_status, new_status);
                let likesCount = result['likes_count']
                $(`#likes-count-${post_id}`).text(`${likesCount} likes`);
            },
        })
    })
  
});