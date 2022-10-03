import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import Login from './components/Login'
import Register from './components/Register'
import Home from './components/Home'
import Account from './components/Account'

const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path: '/login',
  name: 'login',
  component: Login
},
{
  path: '/register',
  name: 'register',
  component: Register
},
{
  path: '/home',
  name: 'home',
  component: Home
},
{
  path: '/cuenta',
  name: 'account',
  component: Account
}]

const history = createWebHistory()

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
