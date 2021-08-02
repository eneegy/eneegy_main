import Home from './Home.vue';
$(function() {
    var app = new Vue({
        vuetify: new Vuetify(),
        el: '#app',
        render: h => h(Home),
    });
});

