<template>
    <div class="register">
      <h1 class="title">Registrarse</h1>
      <form action class="form" @submit.prevent="register">
        <label class="form-label" for="#name">Nombres:</label>
        <input
          v-model="user.name"
          class="form-input"
          type="name"
          id="name"
          required
          placeholder="Nombres"
        >
        <label class="form-label" for="#apellidos">Apellidos:</label>
        <input
          v-model="user.apellidos"
          class="form-input"
          type="apellidos"
          id="apellidos"
          required
          placeholder="Apellidos"
        >
        <label class="form-label" for="#email">Email:</label>
        <input
          v-model="user.email"
          class="form-input"
          type="email"
          id="email"
          required
          placeholder="Email"
        >
        <label class="form-label" for="#password">Password:</label>
        <input
          v-model="user.password"
          class="form-input"
          type="password"
          id="password"
          placeholder="Password"
        >
        <label class="form-label" for="#password-repeat">Repite la contraeña:</label>
        <input
          v-model="user.passwordRepeat"
          class="form-input"
          type="password"
          id="password-repeat"
          placeholder="Password"
        >
        <input class="form-submit" type="submit" value="Registrarse">
      </form>
    </div>
  </template>
  
<script>
  import axios from 'axios';

  export default {
    name: 'register',
  
    data: () => ({
      user: {
        name: '',
        apellidos: '',
        email: '',
        password: '',
        passwordRepeat: ''
      }
    }),
    methods: {
      register() {
        axios.post('api/auth/register', 
          this.user,
          {headers: {}}
        ).then((result) => {
          let dataRegister = {
            name: this.user.name,
            apellidos: this.user.apellidos,
            email: this.user.email,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          }
          this.$emit('completedSignUp', dataRegister)
        }).catch((error) => {
          console.log(error)
          alert("Error: " + error.message);
        });
      }
    }
  };
</script>
  
  <style lang="scss" scoped>
  .register {
    padding: 2rem;
  }
  .title {
    text-align: center;
  }
  .form {
    margin: 3rem auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 20%;
    min-width: 350px;
    max-width: 100%;
    background: rgba(19, 35, 47, 0.9);
    border-radius: 5px;
    padding: 40px;
    box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
  }
  .form-label {
    margin-top: 2rem;
    color: white;
    margin-bottom: 0.5rem;
    &:first-of-type {
      margin-top: 0rem;
    }
  }
  .form-input {
    padding: 10px 15px;
    background: none;
    background-image: none;
    border: 1px solid white;
    color: white;
    &:focus {
      outline: 0;
      border-color: #1ab188;
    }
  }
  .form-submit {
    background: #1ab188;
    border: none;
    color: white;
    margin-top: 3rem;
    padding: 1rem 0;
    cursor: pointer;
    transition: background 0.2s;
    &:hover {
      background: #0b9185;
    }
  }
  .error {
    margin: 1rem 0 0;
    color: #ff4a96;
  }
  </style>