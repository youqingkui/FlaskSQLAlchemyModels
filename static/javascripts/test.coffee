$(document).ready () ->
  $("#get_db").click ->
    reqData = getInfo()
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

  $('#database').change () ->
    dbName = $(this).val()
    reqData = getInfo()
    reqData.db_name = dbName
    $.post '/get_tb', reqData, (body) ->
      data = JSON.parse(body)
      console.log(data)
      if data.msg is 'ok'
        $('#tb_name').html('')
        $.each data.data, (index, tbName) ->
          $('#tb_name').append "<option value=#{tbName}>#{tbName}</option>"

        alert("获取数据库成功")

      else
        alert(data.msg)


  $('#tb_name').change () ->
    dbName = $("#database").val()
    tbName = $(this).val()
    reqData = getInfo()
    reqData.tb_name = tbName
    reqData.db_name = dbName
    $.post '/get_sql_code', reqData, (body) ->
      data = JSON.parse(body)
      console.log data




  getInfo = () ->
    reqData = {}
    reqData.host = $("#host").val()
    reqData.name = $("#name").val()
    reqData.password = $("#password").val()
    reqData.port = $("#port").val()
    return reqData



