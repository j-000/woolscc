import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home'
import CV from './components/CV'


Vue.use(Router)


export default new Router({
  mode: 'history',
  routes:[
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/cv',
      name: 'cv',
      component: CV
    },
    {
      path: '*',
      redirect:{
        name: 'home'
      }
    }
  ]
})