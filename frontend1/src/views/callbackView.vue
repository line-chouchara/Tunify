<!-- callbackView.vue -->
<script lang="js">

    export default {
        mounted() {
            console.log('Composant callback monté.');  //  débogage

            const hashParams = window.location.hash.substr(1).split('&').reduce((result, item) => {
                const parts = item.split('=');
                result[parts[0]] = parts[1];
                return result;
            }, {});
            
            console.log('hashParams:', hashParams); 

            if (hashParams.access_token) {
                console.log('Token trouvé dans hashParams.');  //  débogage

                this.authorize.accessToken = hashParams.access_token;
                this.authorize.tokenType = hashParams.token_type;
                this.authorize.expiredIn = hashParams.expires_in;
                this.authorize.state = hashParams.state;

                this.setTokenLocal();
            } else {
                console.log('Token non trouvé dans hashParams.');  //  débogage
            }
        },
       // components: {
       //     RouterLink,
      //  },
        data() {
            return {
                authorize: {
                    accessToken: null,
                    tokenType: null,
                    expiredIn: null,
                    state: null,
                },
            }
        },
        methods: {
            setTokenLocal: function(){
                console.log('Définir le token dans le localStorage.');  //  débogage

                localStorage.setItem("authCode", JSON.stringify(this.authorize))
                this.$router.replace('/trending')

                console.log('Redirection vers /trending.');  //  débogage
            },
        }
    }
</script>

<template>
    <div></div>
  </template>