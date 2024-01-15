<template>
    <v-app style="background-color: #F2F2F7;">

        <div style="margin: 20px;"
          v-if="departments.length > 0"
        >
            <nav-button
                icon="mdi-alpha-d-box-outline"
                @open-dialog="dialog = !dialog"
            />
            <v-card
                elevation="0"
                color="white"
                width="100%"
                style="border-radius: 10px; margin-top: 20px"
                v-if="!isLoading"
            >
                <v-simple-table>
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th
                                    v-for="(item, i) in headers"
                                    :key="i"
                                >
                                    {{ item }}
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="(item, i) in departments"
                                :key="i"
                                :style="i % 2 === 0 ? 'background-color: #F2F2F7': ''"
                                class="table-row"

                            >
                                <td>{{ item.id }}</td>
                                <td>{{ item.name }}</td>
                                <td style="width: 125px">
                                    <v-btn icon style="border: 1px solid #AEAEAE" class="ml-1" @click="deleteDep(item.id)">
                                        <v-icon size="25">mdi-delete-outline</v-icon>
                                    </v-btn>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card>

            <v-dialog
                v-model="dialog"
                transition="dialog-bottom-transition"
                max-width="20%"
            >
                <v-card
                    elevation="0"
                    class="pa-6"
                >
                    <v-text-field
                        outlined
                        hide-details
                        dense
                        v-model="department.name"
                        label="department"
                    />
                    <v-row no-gutters class="mt-3">
                        <v-spacer/>
                        <v-btn elevation="0" color="#0BB923" dark @click="postData">Save</v-btn>
                    </v-row>
                </v-card>
            </v-dialog>

        </div>
      <div style="width: 100%; height: 100%; display: flex; justify-content: center;align-items: center">
        <v-img
            v-if="departments.length === 0 && !isLoading"
            src="@/assets/no-data.png"
            style="position: absolute;width: 50%"
        />
      </div>
      <loading-animation v-if="isLoading"/>
    </v-app>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';
import NavButton from '@/components/example/NavButton.vue';
import LoadingAnimation from "@/components/example/LoadingAnimation.vue";

export default {
    data: () => ({
        headers: ['ID', 'bölümi', 'action'],
        departments: [],
        department: {},
        dialog: false,
        isLoading: true,
        Toast: Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 1500,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            },
        }),
    }),
    created() {
        this.getDepartment()
    },
    methods: {
        async getDepartment() {
            await axios.get('/department/')
            .then((res) => {
                this.departments = res.data.data
                this.isLoading = false
            })
            .catch((err) => {
                console.log(err)
            })
        },

        async postData() {
            await axios.post('/department/', {
                name: this.department.name
            })
            .then(() => {
                this.dialog = !this.dialog
                this.getDepartment()
                this.Toast.fire({
                    icon:'success',
                    title: 'Successfully saved'
                })
                this.department = {}
            })
            .catch((err) => {
                console.log(err)
                this.dialog = !this.dialog
                this.department = {}
            })
        },
        
        deleteDep(id) {
            Swal.fire({
                title: 'Are you sure?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#7FBA5E',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, delete it!'
            })
            .then((res) => {
                if(res.isConfirmed) {
                    axios.delete(`/department/${id}/`)
                    .then(() => {
                        this.Toast.fire({
                            icon:'success',
                            title: 'Successfully deleted'
                        })
                        this.getDepartment()
                    })
                    .catch((err) => {
                        console.log(err)
                        this.Toast.fire({
                            icon:'error',
                            title: 'Something went wrong'
                        })
                    })
                }
            })
        }
    },
    components: {
        NavButton,
      LoadingAnimation
    }
}
</script>

<style scoped>

</style>