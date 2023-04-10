<template>
    <div class="flex min-h-screen min-w-screen bg-[#1f1f1f]  " >
        <hea-der class="" />
        <div class="flex h-full w-full">
          <top-ter class="fixed z-30 pl-[250px]" />
          <div class="pl-[250px] w-full">
            <router-view :class="{'justify-end bg-[#5038A0] px-0 py-0':counter.Path_Route.path=='/Love-Song','bg-sky-500 px-0 py-0':counter.Path_Route.path=='/Play-list','px-3 py-3':counter.Path_Route.path=='/Search'||'/'}" class=" my-[64px]  w-full "/>
          </div>
        </div>
        <foo-ter class="fixed w-full bottom-0 z-50" />
        <div v-if="counter.Show_Table_Login==0" class="bg-zinc-900 fixed z-50 inset-0 flex flex-col items-center justify-center">
          <img src="@/assets/transparent_white.png" class="w-[230px] mb-[25px]"/>
          <div class="flex flex-col justify-center items-center   w-[350px] gap-3">
            <div v-show="counter.Login_SignUp==1" class="flex flex-col justify-center items-center   w-[350px] gap-3">
              <h1 class="text-[35px] text-white font-bold">Đăng nhập</h1>
              <div class="flex flex-col text-gray-300 w-full gap-1">
                <!-- <h1>Tên tài khoản</h1> -->
                <input placeholder = "Tên tài khoản" class="rounded h-[35px] w-full bg-zinc-700 px-2" v-model="counter.username"/>
                <!-- <h1 class="text-[13px] font-light text-center text-lime-600">Chúng tôi sẽ không bao giờ chia sẻ thông tin chi tiết của bạn với bất kỳ ai khác.</h1> -->
              </div>
              <div class="flex flex-col text-gray-300 w-full gap-1">
                <!-- <h1>Mật khẩu</h1> -->
                <input placeholder = "Mật khẩu" type="password" class="rounded h-[35px] w-full bg-zinc-700 px-2" v-model="counter.password"/>
              </div>
              <button v-on:click="counter.Get_Data_User(); counter.get_song_play_list();" class="bg-sky-600  rounded w-full text-gray-200 h-[35px] font-bold mt-5">Đăng nhập</button>
              <!-- <button class="flex justify-center items-center gap-2 border-2 border-sky-600  rounded w-full text-sky-600 font-medium h-[35px] bg-transparent"><img src="@/assets/gg.png" class="w-[25px]"/><h1>Đăng nhập cùng với Google</h1></button> -->
            </div>
            <div v-show="counter.Login_SignUp==2" class="flex flex-col justify-center items-center   w-[350px] gap-3">
              <h1 class="text-[35px] text-white font-bold">Đăng kí</h1>
              <div class="flex flex-col text-gray-300 w-full gap-1">
                <!-- <h1>Email</h1> -->
                <input placeholder = "Email" v-model="counter.email_dk" class="rounded h-[35px] w-full bg-zinc-700 px-2"/>
                <!-- <h1 class="text-[13px] font-light text-center text-lime-600">Chúng tôi sẽ không bao giờ chia sẻ thông tin chi tiết của bạn với bất kỳ ai khác.</h1> -->
              </div>
              <div class="flex flex-col text-gray-300 w-full gap-1">
                <!-- <h1>Tên tài khoản</h1> -->
                <input placeholder = "Tên tài khoản" v-model="counter.username_dk" class="rounded h-[35px] w-full bg-zinc-700 px-2"/>
                <!-- <h1 class="text-[13px] font-light text-center text-lime-600">Chúng tôi sẽ không bao giờ chia sẻ thông tin chi tiết của bạn với bất kỳ ai khác.</h1> -->
              </div>
              <div class="flex flex-col text-gray-300 w-full gap-1">
                <!-- <h1>Mật khẩu</h1> -->
                <input placeholder = "Mật khẩu" type="password" v-model="counter.password_dk" class="rounded h-[35px] w-full bg-zinc-700 px-2"/>
              </div>
              <button v-on:click="counter.Set_Data_User();" class="bg-sky-600  rounded w-full text-gray-200 h-[35px] font-bold mt-5">Đăng kí</button>
            </div>
            <h1 v-on:click="counter.Login_SignUp=2" v-show="counter.Login_SignUp==1" class="text-lime-500 underline font-normal cursor-pointer">Đăng kí tài khoản</h1>
            <h1 v-on:click="counter.Login_SignUp=1" v-show="counter.Login_SignUp==2" class="text-lime-500 underline font-normal cursor-pointer">Đăng nhập tài khoản</h1>
            <!-- <h1>{{ counter.Show_Table_Login }}</h1> -->
          </div>
        </div>
    </div>
</template>
  

  <script>
  // Import thành phần (components) NavBar, SideBar, FooterBar để sử dụng
  import HeaDer from '@/components/HeaDer.vue'
  import FooTer from '@/components/FooTer.vue'
  import TopTer from '@/components/TopTer.vue'

  import { useCounterStore } from '@/stores/counter';

  
  // Để sử dụng được các thẻ (tag) của các component tương ứng
  // <nav-bar />     -> component NavBar
  // <side-bar />    -> component SideBar
  // <footer-bar />  -> component FooterBar
  // Chúng ta phải khai báo trong thuộc tính `components` của phần export default {}
  export default {
    setup() {
    const counter = useCounterStore();
    return {counter}
  },
    components: {
      HeaDer,
      FooTer,
      TopTer,
    }
  }
  </script>
  
<style>
body::-webkit-scrollbar {
  width: 14px;               /* Chiều rộng vùng chứa scrollbar */
}
body::-webkit-scrollbar-track {
  background: #393636;        /* Màu nền ngoài của thanh scrollbar */
}
body::-webkit-scrollbar-thumb {
  background-color: #686867;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
body::-webkit-scrollbar-thumb:hover {
    background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}
</style>