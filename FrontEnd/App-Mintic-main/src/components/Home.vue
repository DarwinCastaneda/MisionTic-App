<template>

    <div class="greetings">
        <h1>¡Bienvenido  <span> {{name}} {{ apellidos}} </span>!</h1>
    </div>

</template>
 
<script>

export default {
    name: "home",

    data: function(){
        return {
            name: localStorage.getItem('name') || "none",
            apellidos: localStorage.getItem('apellidos') || "none"
        }
    }
}

</script>
 
<style>
    .greetings{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
    
        display: flex;
        justify-content: center; 
        align-items: center;
    }

    .greetings h1{
        font-size: 50px;
        color: #283747;
    }

    .greetings span{
        color: crimson;
        font-weight: bold;
    }
</style>
