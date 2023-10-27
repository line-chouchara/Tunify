<!--footer_comp.vue-->
<template>
    <footer class="footer">
        <div class="footer-container">
            <div class="content">
                <p>&copy; 2021 Tunify</p>
                <ul class="footer-links">
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Use</a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </div>
        </div>
    </footer>
</template>

<style scoped>
    .footer {
        background-color: #FD5E64;
        padding: 20px 0;
        color: white;
        font-weight: 500;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
        width: 100%;
        margin: 0;
    }

    .footer-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin: 0 auto;
        padding: 0 15px; /* Allow some spacing for inner content but not affecting the outer width */
        max-width: 1200px; /* This can be adjusted based on your design preference */
    }

    .footer-links {
        display: flex;
        gap: 15px;
        list-style: none;
        padding: 0;
    }

    .footer-links li a {
        color: white;
        transition: color 0.3s;
        text-decoration: none;
        border-bottom: 2px solid transparent;
    }

    .footer-links li a:hover {
        color: #FFFAFA;
        border-bottom-color: #FFFAFA;
    }
</style>
