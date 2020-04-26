<html>
   <head>
      <title>VueJs Instance</title>
      <script type = "text/javascript" src = "js/vue.js"></script>
   </head>
   <body>
      <div id = "vue_det">
         <h1>Firstname : {{firstname}}</h1>
         <h1>Lastname : {{lastname}}</h1>
         <div>{{htmlcontent}}</div>
      </div>
      <script type = "text/javascript" src = "js/vue_template.js"></script>
   </body>
</html>
<script>
var vm = new Vue({
   el: '#vue_det',
   data: {
      firstname : "Ria",
      lastname  : "Singh",
      htmlcontent : "<div><h1>Vue Js Template</h1></div>"
   }
})
</script>