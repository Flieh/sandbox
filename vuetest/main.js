'use strict'

var growler = new Vue({
  el: '#growler',
  data: {
    appName: 'Todos'
  }
})

var todos = new Vue({
  el: '#todos',
  data: {
    todos: [
      { text: 'Learn JavaScript' },
      { text: 'Learn Vue' },
      { text: 'Build Something Awesome' }
    ]
  }
})