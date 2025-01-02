<template>
    <router-view/>
</template>

<script>
    export default {
        name: 'App'
    }
</script>


<style>
    #articles {
        padding: 10px;
    }

    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
    
    .tag {
        padding: 2px 5px 2px 5px;
        margin: 5px 5px 5px 0;
        font-family: Georgia, Arial, sans-serif;
        font-size: small;
        background-color: #4e4e4e;
        color: whitesmoke;
        border-radius: 5px;
    }
    
    #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 40px;
        margin-right: 40px;
    }
    
    #header {
        text-align: center;
        margin-top: 20px;
    }
    
    #footer {
        position: fixed;
        left: 0;
        bottom: 0;
        height: 50px;
        width: 100%;
        background: whitesmoke;
        text-align: center;
        font-weight: bold;
    }
</style>


