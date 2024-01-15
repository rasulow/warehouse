<template>
    <v-app style="background-color: #F2F2F7;">
        <div style="margin: 20px;">
            <nav-button
                icon="mdi-alpha-u-box-outline"
                @open-dialog="dialog = !dialog"
                :showType="true"
                @change-type="getUsers"
            />
            <!-- table -->
            <v-card
                elevation="0"
                color="white"
                width="100%"
                style="border-radius: 10px; margin-top: 20px"
                v-if="!isLoading & users.length > 0"
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
                                v-for="(item, i) in users"
                                :key="i"
                                :style="i % 2 == 0 ? 'background-color: #F2F2F7': ''"
                                class="table-row"

                            >
                                <td>{{ item.id }}</td>
                                <td>{{ item.department?.name }}</td>
                                <td>{{ item.position?.name }}</td>
                                <td>{{ item.username }}</td>
                                <td>{{ item.staff_id }}</td>
                                <td>
                                    <v-switch
                                        v-model="item.is_deleted"
                                        inset
                                        color="#0BB923"
                                        :ripple="false"
                                        @change="updateIsDeleted(item.id, item.is_deleted)"
                                    />
                                </td>
                                <td style="width: 125px">
                                    <v-btn icon style="border: 1px solid #AEAEAE" class="ml-1" @click="deleteUser(item.id)">
                                        <v-icon size="25">mdi-delete-outline</v-icon>
                                    </v-btn>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card> 

            <!-- dialog -->
            <v-dialog
                v-model="dialog"
                transition="dialog-bottom-transition"
                max-width="20%"
            >
                <v-card 
                    elevation="0"
                    class="pa-6"
                >
                    <v-combobox
                        dense
                        outlined
                        label="department"
                        v-model="user.department"
                        :items="departments"
                        item-text="name"
                        clearable
                    />
                    <v-combobox
                        dense
                        outlined
                        label="position"
                        v-model="user.position"
                        :items="positions"
                        item-text="name"
                        clearable
                    />
                    <v-text-field
                        outlined
                        dense
                        label="username"
                        v-model="user.username"
                    />
                    <v-text-field
                        outlined
                        dense
                        label="password"
                        v-model="user.password"
                    />
                    <v-combobox
                        dense
                        outlined
                        label="role"
                        v-model="user.role"
                        :items="roles"
                        clearable
                    />
                    <v-text-field
                        outlined
                        hide-details
                        dense
                        label="staff_id"
                        v-model="user.staff_id"
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
            v-if="users.length === 0 && !isLoading"
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
        headers: ['id', 'department', 'position', 'username', 'staff_id', 'is_deleted', 'action'],
        roles: ['admin', 'user'],
        users: [],
        user: {},
        dialog: false,
        departments: [],
        positions: [],
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
        this.getUsers(),
        this.getDepartment(),
        this.getPositions()
    },
    methods: {
        async getUsers(is_deleted) {
            await axios.get('/user/', { params: { is_deleted: is_deleted } })
            .then((res) => {
                this.users = res.data.data
                this.isLoading = false
            })
            .catch((err) => {
                console.log(err)
            })
        },

        async updateIsDeleted(id, is_deleted) {
            await axios.patch(`/user/${id}/`, {
                is_deleted: is_deleted
            })
            .then(() => {
                this.Toast.fire({
                    icon:'success',
                    title: 'Successfully updated'
                })
            })
            .catch((err) => {
                console.log(err)
                this.Toast.fire({
                    icon:'error',
                    title: 'Something went wrong'
                })
            })
        },

        async getDepartment() {
            await axios.get('/department/')
            .then((res) => {
                this.departments = res.data.data
            })
            .catch((err) => {
                console.log(err)
            })
        },

        async getPositions() {
            await axios.get('/position/')
            .then((res) => {
                this.positions = res.data.data
            })
            .catch((err) => {
                console.log(err)
            })
        },

        async postData() {
            await axios.post('/auth/', {
                username: this.user.username,
                password: this.user.password,
                role: this.user.role,
                staff_id: this.user.staff_id,
                department_id: this.user.department.id,
                position_id: this.user.position.id
            })
            .then(() => {
                this.Toast.fire({
                    icon:'success',
                    title: 'Successfully saved'
                })
                this.getUsers()
                this.user = {}
                this.dialog = !this.dialog
            })
            .catch((err) => {
                console.log(err)
                this.Toast.fire({
                    icon:'error',
                    title: 'Something went wrong'
                })
                this.user = {}
                this.dialog = !this.dialog
            })
        },

        deleteUser(id) {
            Swal.fire({
                title: 'Are you sure?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#7FBA5E',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, delete it!'
            })
            .then((res) => {
                if (res.isConfirmed) {
                    axios.delete(`/user/${id}/`)
                    .then(() => {
                        this.Toast.fire({
                            icon:'success',
                            title: 'Successfully deleted'
                        })
                        this.getUsers()
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
      LoadingAnimation,
        NavButton
    }
}
</script>

<style scoped>

</style>