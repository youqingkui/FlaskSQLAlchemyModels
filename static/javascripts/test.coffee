$(document).ready () ->
  $("#get_db").click ->
    reqData = {}
    reqData.host = $("#host").val()
    reqData.name = $("#name").val()
    reqData.password = $("#password").val()
    reqData.port = $("#port").val()

    $.post '/get_db', reqData, (body) ->
      console.log(body)
      data = JSON.parse(body)
      console.log(data)
      if data.msg is 'ok'
        $('#database').html('')
        $.each data.data, (index, dbName) ->
          $('#database').append "<option value=#{dbName}>#{dbName}</option>"

        alert("获取数据库成功")

      else
        alert(data.msg)



