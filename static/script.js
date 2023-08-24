const getStreams = async ()=>{
    let url = $("#mediaUrl").val()
    let response = await fetch("/getStreams?url="+url)
    let responseText = await response.text()
    $("#query").css("display", "unset")
    $("#query").html("<h1>"+ responseText + "</h1>")
}
const getDownload = async (media, resolution )=>{
    const request = await fetch(`/getDownload/${media}/${resolution}`)
    const response = await request.text()
    $("#query").html(response)
    //getProgress()
}
    
const getProgress = async()=>{
    alert("Progress bar !!!")
    /*
    let request_progress = fetch("/getProgress")
    let progress = await request_progress.text()
    alert(progress)
    */
}
