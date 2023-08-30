
const validateUrl = () =>{
    let url = $("#mediaUrl").val()
    var p = /^(?:https?:\/\/)?(?:m\.|www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
    if(url.match(p)){
        getStreams(url)
    }
    else{
        $("#mediaUrl").val("")
        alert("Invalid Link ! , Please enter a valid youtube link")
    }
}

const getStreams = async(url_string)=>{
    $("#loading").css("display", "unset")
    let response = await fetch("/getStreams?url="+url_string)
    let responseText = await response.text()  
    $("#loading").css("display", "none")
    $("#mainad").css('display', 'none')
    if(responseText.includes('Error')){
        alert('Error : File is too long , Try uploading shorter videos')
    }else{
        $("#events-wrapper").html(responseText) 
    }
}


const getDownload = async (media, resolution )=>{
    $("#mainad").css('display', 'unset')
    $("#loading").css('display', 'unset')
    const request = await fetch(`/getDownload/${media}/${resolution}`)
    const response = await request.text()
    $("#loading").css('display', 'none')
    $("#download-ready").css("display", "unset")
    $("#download-ready").attr("href",`./static/temp/${response}`)
}

const notification = function(){
    alert('File is being downloaded successfully !')
    location.reload();
}

