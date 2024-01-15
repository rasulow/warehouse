<template>
    <v-app style="background-color: #F2F2F7;">
        <div style="margin: 20px">
            <nav-button
                icon="mdi-alpha-p-box-outline"
                @open-dialog="dialog = !dialog"
                v-if="positions.length > 0"
            />
            <!-- table -->
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
                                v-for="(item, i) in positions"
                                :key="i"
                                :style="i % 2 == 0 ? 'background-color: #F2F2F7': ''"
                                class="table-row"

                            >
                                <td>{{ item.id }}</td>
                                <td>{{ item.department.name }}</td>
                                <td>{{ item.name }}</td>
                                <td style="width: 125px">
                                    <v-btn icon style="border: 1px solid #AEAEAE" class="ml-1" @click="deletePos(item.id)">
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
                        label="Bölümi"
                        v-model="position.department"
                        :items="departments"
                        item-text="name"
                        clearable
                    />
                    <v-text-field
                        outlined
                        hide-details
                        dense
                        v-model="position.name"
                        label="weizpesi"
                    />
                    <v-row no-gutters class="mt-3">
                        <v-spacer/>
                        <v-btn elevation="0" color="#0BB923" dark @click="postData">Ýatda sakla</v-btn>
                    </v-row>
                </v-card>
            </v-dialog>
        </div>

      <div style="width: 100%; height: 100%; display: flex; justify-content: center;align-items: center">
        <v-img
            v-if="positions.length === 0 && !isLoading"
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
        headers: ['ID', 'Bölümi', 'wezipesi', 'action'],
        positions: [],
        position: {},
        departments: [],
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
        this.getPosition(),
        this.getDepartment()
    },
    methods: {
        async getPosition() {
            await axios.get('/position/')
            .then((res) => {
                this.positions = res.data.data
                this.isLoading = false
            })
            .catch((err) => {
                console.log(err)
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

        async postData() {
            await axios.post('/position/', {
                name: this.position.name,
                department_id: this.position.department.id
            })
            .then(() => {
                this.dialog = !this.dialog
                this.getPosition()
                this.Toast.fire({
                    icon:'success',
                    title: 'Successfully saved'
                })
                this.position = {}
            })
            .catch((err) => {
                console.log(err)
                this.dialog = !this.dialog
                this.position = {}
            })
        },

        deletePos(id) {
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
                    axios.delete(`/position/${id}/`)
                    .then(() => {
                        this.Toast.fire({
                            icon:'success',
                            title: 'Successfully deleted'
                        })
                        this.getPosition()
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