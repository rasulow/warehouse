import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/pages/Login/LoginPage.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/views/pages/Dashboard/DashboardPage.vue')
  },
  {
    path: '/user',
    name: 'user',
    component: () => import('@/views/pages/UserPage.vue')
  },
  {
    path: '/department',
    name: 'department',
    component: () => import('@/views/pages/DepartmentPage.vue')
  },
  {
    path: '/position',
    name: 'position',
    component: () => import('@/views/pages/PositionPage.vue')
  },
  {
    path: '/item',
    name: 'item',
    component: () => import('@/views/pages/ItemPage.vue')
  },
  {
    path: '/requests',
    name: 'requests',
    component: () => import('@/views/pages/RequestPage.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
