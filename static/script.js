
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
    $("#search-wrapper").css("display", "none")
    $("footer").css("display", "none")
    $("#loading").css("display", "unset")
    let response = await fetch("/getStreams?url="+url_string)
    let responseText = await response.text()  
    $("#loading").css("display", "none")
    $("#mainad").css('display', 'none')
    if(responseText.includes('Error')){
        alert('Error : File is too long , Try uploading shorter videos')
    }else{
        $("#events-wrapper").append(responseText)
        }
}
const getDownload = async (media, resolution )=>{
    $("#mainad").css('display', 'unset')
    $("#events-wrapper > *:not(#loading)").html("")
    $("#loading").css('display', 'block')
    const request = await fetch(`/getDownload/${media}/${resolution}`)
    const response = await request.text()
    $("#loading").css('display', 'none')
    let download = `<a id='downloadready' onclick='notification()' href='/static/temp/${response}' download><p class='mssg'>Download</p></a>`
    $("#events-wrapper").html(download)
}
const notification = function(){
    alert('File is being downloaded successfully !')
    window.open("","_blank")
    location.reload();
}

