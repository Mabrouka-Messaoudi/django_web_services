import { createRouter, createWebHistory } from 'vue-router';

import RegisterForm from "@/components/RegisterForm.vue";
import LoginForm from "@/components/LoginForm.vue";
import TripsApp from "@/components/TripsApp.vue";
import UserReservation from "@/components/UserReservation.vue";
import Aboutus from "@/components/Aboutus.vue";
import HomeVue from "@/components/HomePage.vue";
import clientList from "@/components/clientList.vue";
import AdminPanel from "@/components/AdminPanel.vue";
function isAuthenticated() {
    const token = localStorage.getItem('auth_token');
    return token ? true : false;
}

// Define routes
const routes = [
    { path: "/login", component: LoginForm },
    { path: "/register", component: RegisterForm },
    { path: "/aboutus", component: Aboutus },
    { path: "/clients", component: clientList },
    { path: "/admin", component: AdminPanel },
    { path: "/", component: HomeVue },
    {
        path: "/trips",
        component: TripsApp,
        meta: { requiresAuth: false },  // This route requires authentication
    },
    { path: "/reservation", component: UserReservation, meta: { requiresAuth: true } },


];

// Create the router
const router = createRouter({
    history: createWebHistory(),
    routes,
});
// Global route guard to check if authentication is required
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!isAuthenticated()) {
            // Redirect to login page if not authenticated
            next('/login');
        } else {
            next(); // Proceed to the requested route
        }
    } else {
        next(); // No authentication required, proceed to the route
    }
});


export default router;
