
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
    $("#loading-streams").css("display", "unset")
    let response = await fetch("/getStreams?url="+url_string)
    let responseText = await response.text()  
    $("#loading-streams").css("display", "none")
    $("#mainad").css('display', 'none')
    $("#events-wrapper").html(responseText) 
}


const getDownload = async (media, resolution )=>{
    $("#mainad").css('display', 'unset')
    $("#events-wrapper").html("<p class='mssg' >Getting Your Download , Please Wait</p>")
    const request = await fetch(`/getDownload/${media}/${resolution}`)
    const response = await request.text()
    let msgHTML = "<a onclick='notification()' href='"+ response +"' download><p class='mssg download'>Download</p></a>" 
    $("#events-wrapper").html(msgHTML)
}

const notification = function(){
    alert('File is being downloaded successfully !')
    location.reload();
}

