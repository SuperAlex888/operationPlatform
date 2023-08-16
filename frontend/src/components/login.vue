<template>
  <body translate="no">
    <div class="wrapper fadeInDown">
    <div id="formContent">
      <!-- Tabs Titles -->
      <h2 class="active"> 登录界面 </h2>
      <h2 class="inactive underlineHover">v_v</h2>
  
      <!-- Icon -->
      <!-- <div class="fadeIn first">
        <img src="http://danielzawadzki.com/codepen/01/icon.svg" id="icon" alt="User Icon">
      </div> -->
  
      <!-- Login Form -->
      <form>
        <input v-model.lazy="account" type="text" id="login" class="fadeIn second" name="login" placeholder="login">
        <input  v-model.lazy="password" type="text" id="password" class="fadeIn third" name="login" placeholder="password">
        <input @click="login" type="submit" class="fadeIn fourth" value="Log In">

      </form>
  
      <!-- Remind Passowrd -->
      <div id="formFooter">
        <a class="underlineHover" href="#">启联运维平台</a>
      </div>
  
    </div>
  </div>
</body>
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
@import url(../assets/login.css);
</style>