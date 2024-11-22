<template>
    <div class="userinfo-container">
      <h2>User Information</h2>
      <div v-if="user">
        <div class="userinfo-detail">
          <p><strong>Username:</strong> {{ user.username }}</p>
          <p><strong>Email:</strong> {{ user.email }}</p>
          <p><strong>Password:</strong> {{ user.password }}</p>
        </div>
        <button class="btn btn-modify" @click="openModifyModal">Modify</button>
      </div>
      <div v-else>
        <p>Loading user information...</p>
      </div>
  
      <!-- 修改用户信息模态框 -->
      <div v-if="showModifyModal" class="modal-overlay">
        <div class="modal-content">
          <h3>Modify User Information</h3>
          <form @submit.prevent="submitModification">
            <label>
              Username:
              <input type="text" v-model="form.username" />
            </label>
            <label>
              Email:
              <input type="email" v-model="form.email" />
            </label>
            <label>
              Password:
              <input type="password" v-model="form.password" />
            </label>
            <button class="btn btn-save" type="submit">Save</button>
            <button class="btn btn-cancel" type="button" @click="closeModifyModal">Cancel</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserinfoPage",
    data() {
      return {
        user: null, // 用户信息
        showModifyModal: false, // 控制模态框显示
        form: {
          user_id: null,
          username: "",
          email: "",
          password: "",
        },
        // 默认用户数据，供后端未响应时使用
        defaultUser: {
          user_id: 1,
          username: "defaultuser",
          email: "default@example.com",
          password: "defaultpassword",
        },
      };
    },
    methods: {
      async fetchUserInfo() {
        try {
          const response = await fetch("http://127.0.0.1:8000/user/user_info/", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          });
  
          if (response.ok) {
            const data = await response.json();
            if (data.success) {
              this.user = data.data;
              this.form = { ...data.data };
            } else {
              console.warn("Failed to fetch user info. Using default data.");
              this.useDefaultUser();
            }
          } else {
            console.warn("HTTP error. Using default data.");
            this.useDefaultUser();
          }
        } catch (error) {
          console.error("Error fetching user info:", error);
          this.useDefaultUser();
        }
      },
      useDefaultUser() {
        // 使用默认数据
        this.user = this.defaultUser;
        this.form = { ...this.defaultUser };
      },
      openModifyModal() {
        this.showModifyModal = true;
      },
      closeModifyModal() {
        this.showModifyModal = false;
      },
      async submitModification() {
        try {
          const response = await fetch("http://127.0.0.1:8000/user/user_info_modify/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(this.form),
          });
  
          if (response.ok) {
            const data = await response.json();
            if (data.success) {
              alert(data.message); // 修改成功提示
              this.user = { ...this.form }; // 更新用户信息
              this.closeModifyModal(); // 关闭模态框
            } else {
              console.error("Modification failed:", data.message);
            }
          } else {
            console.error("HTTP error during modification.");
          }
        } catch (error) {
          console.error("Error submitting modification:", error);
          alert("Modification failed. Please try again.");
        }
      },
    },
    created() {
      this.fetchUserInfo(); // 加载用户信息
    },
  };
  </script>
  
  <style scoped>
  .userinfo-container {
    text-align: center;
    padding: 2rem;
  }
  
  .userinfo-detail p {
    margin: 1rem 0;
  }
  
  .btn {
    display: inline-block;
    margin: 1rem 0.5rem;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .btn-modify {
    background-color: #5bc0de;
    color: white;
  }
  
  .btn-save {
    background-color: #5cb85c;
    color: white;
  }
  
  .btn-cancel {
    background-color: #d9534f;
    color: white;
  }
  
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .modal-content {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    width: 400px;
    text-align: left;
  }
  
  label {
    display: block;
    margin: 1rem 0;
  }
  
  input {
    width: 100%;
    padding: 0.5rem;
    margin-top: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
  }
  </style>
  