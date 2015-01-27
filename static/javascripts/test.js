// Generated by CoffeeScript 1.8.0
(function() {
  $(document).ready(function() {
    return $("#get_db").click(function() {
      var reqData;
      reqData = {};
      reqData.host = $("#host").val();
      reqData.name = $("#name").val();
      reqData.password = $("#password").val();
      reqData.port = $("#port").val();
      return $.post('/get_db', reqData, function(body) {
        var data;
        console.log(body);
        data = JSON.parse(body);
        console.log(data);
        if (data.msg === 'ok') {
          $('#database').html('');
          $.each(data.data, function(index, dbName) {
            return $('#database').append("<option value=" + dbName + ">" + dbName + "</option>");
          });
          return alert("获取数据库成功");
        } else {
          return alert(data.msg);
        }
      });
    });
  });

}).call(this);

//# sourceMappingURL=test.js.map