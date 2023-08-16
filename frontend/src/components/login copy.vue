<template>
  <h1>启联运维平台</h1>
  <input v-model.lazy="account" type="text" placeholder="请输入账号">
  <input v-model.lazy="password" type="text" placeholder="请输入密码">
  <button @click="login">login</button>

</template>

<script>
window.console = window.console || function(t) {};


export default{
  data(){
    return{
        account:"",
        password:"",
        token:null,

    }},
    methods:{
      login(event){
        var that=this;
        var params = new URLSearchParams();
        params.append('account',this.account);
        params.append('password',this.password);
        that.$axios({
          method:'post',
          url:"http://127.0.0.1:8000/auth/login",
          data:params,
        }).then(function(response){
            var csrf_token = response.headers['csrf_token'];
      
            if(response.status === 200){
              console.log("登录成功");
              var csrf_token = response.headers['csrf_token'];
              that.token = csrf_token;
              console.log(csrf_token)
            }
            else{
              console.log("账号密码错误！")
            }
        }).catch(function(error){
          console.log("账号密码错误");
        })
      }}
}
</script>

<style scoped>

</style>