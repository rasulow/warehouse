import Swal from "sweetalert2"
import axios from "axios";

export default {
    data: () => ({
        show1: false,
        password: '',
        username: '',
        usernameRules: [
            v => !!v || 'Ulanyjy ady hökman!',
            v => v.length <= 10 || 'Ulanyjy ady 10 simwoldan az bolmaly!',
        ],
        passwordRules: [
          v => !!v || 'Açar sözi hökman!',
          v => v.length <= 10 || 'Açar sözi 10 simwoldan az bolmaly!',
        ],
        Toast: Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 1500,
          timerProgressBar: true,
          didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
          }
        })
    }),
    created() {
      this.deleteToken();
    },
    methods: {
      
      async deleteToken() {
        localStorage.removeItem('token')
      },
      async login() {
        const formData = new FormData()
          formData.append('username', this.username)
          formData.append('password', this.password)
          axios.post('/auth/token/', formData,
              {
                  headers: {
                      'Content-Type': 'application/x-www-form-urlencoded'
                  }
              })
              .then((res) => {
                  if (res.data.role === 'admin') {
                      localStorage.setItem('token', res.data.access_token)
                      this.Toast.fire({
                          icon: 'success',
                          title: 'Üstünlikli ulgama girdiňiz!'
                      })
                      this.$router.push('/dashboard')
                  } else {
                      this.username = ''
                      this.password = ''
                      this.Toast.fire({
                          icon: 'error',
                          title: 'Siziň ulanyjyňyzda administratiw hukugy ýok!'
                      })
                  }
              })
              .catch((err) => {
                  console.log(err)
                  this.username = ''
                  this.password = ''
                  this.Toast.fire({
                      icon: 'error',
                      title: 'Ýalňyşlyk ýüze çykdy!'
                  })
              })
      }
    }
  }