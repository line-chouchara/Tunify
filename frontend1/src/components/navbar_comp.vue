<!--navbar_comp.vue-->
<template>
    <nav class="navbar">
        <!-- Site Logo -->
        <div class="logo">
            <router-link to="/">
                <span class="site-name">Tunify</span>
            </router-link>
        </div>

        <!-- Authentication Button on the right -->
        <div class="auth-container">
            <router-link v-if="!isAuthenticated" to="/signup">
                <button class="auth-button">Authentification</button>
            </router-link>
            <router-link v-if="isAuthenticated" to="/discover">
                <button class="nav-button">Discover</button>
            </router-link>
            <router-link v-if="isAuthenticated" to="/trending">
                <button class="nav-button">Trending</button>
            </router-link>
            <button v-if="isAuthenticated" @click="logout" class="auth-button">Déconnexion</button>
        </div>
    </nav>
</template>

<script>
import apiClient from '@/api.js';
export default {
    data() {
        return {
            isAuthenticated: false
        }
    },
    methods: {
        checkAuthentication() {
            const tokenValid = localStorage.getItem('authCode');
            this.isAuthenticated = tokenValid !== null;
        },
        async logout() {
            try {
                await apiClient.logout(); // Call the API for logout
                localStorage.removeItem('authCode');
                this.isAuthenticated = false;
                this.$router.push('/'); // Redirect to home page after logout
            } catch (error) {
                console.error('Error during logout:', error);
            }
        }
    },
    mounted() {
        this.checkAuthentication();
    },
    watch: {
        $route() {
            this.checkAuthentication();
        }
    }
}
</script>


<style scoped>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #FD5E64;
        padding: 15px 0; /* Remove horizontal padding */
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
        width: 100%;
        margin: 0; /* Ensure no margin */
        transition: all 0.3s ease;
    }

    .navbar:hover {
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
    }

    .logo {
        display: flex;
        align-items: center;
        padding-left: 30px; /* Add padding to the logo for better placement */
    }

    .site-name {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: 1.2px;
        color: white;
        text-transform: uppercase;
    }

    .auth-container {
        padding-right: 30px; /* Add padding to the auth button for better placement */
    }

    .auth-button {
        background-color: white;
        color: #FD5E64;
        border: 2px solid white;
        padding: 10px 25px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .auth-button:hover {
        transform: translateY(-5px);
        background-color: #FD5E64;
        color: white;
        border: 2px solid white;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    .nav-button {
        background-color: transparent;
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-right: 10px; /* Spacing between buttons */
    }

    .nav-button:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
</style>
