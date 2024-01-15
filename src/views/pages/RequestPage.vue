<template>
    <v-app style="background-color: #F2F2F7;">

        <div style="margin: 20px"

        >
            <v-card
                elevation="0"
                color="white"
                width="100%"
                style="border-radius: 10px; padding: 15px"
            >
                <v-row no-gutters>
                    <v-col cols="12" sm="2" md="2" xs="2">
                        <v-combobox
                            dense
                            outlined
                            hide-details
                            :items="status"
                            v-model="statusModel"
                            label="status"
                            clearable
                            @change="getRequest"
                        />
                    </v-col>
                </v-row>
            </v-card>

            <!-- table -->
            <v-card
                elevation="0"
                color="white"
                width="100%"
                style="border-radius: 10px; margin-top: 20px"
                v-if="!isLoading & requests.length > 0"
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
                                v-for="(item, i) in requests"
                                :key="i"
                                :style="i % 2 === 0 ? 'background-color: #F2F2F7': ''"
                                text-decoration="line-through"
                                class="table-row"
                            >
                                <td @click="openDialog(item)">{{ item.id }}</td>
                                <td @click="openDialog(item)">{{ item.item?.title }}</td>
                                <td @click="openDialog(item)">{{ item.item?.quantity }}</td>
                                <td @click="openDialog(item)">{{ item.req_quantity }}</td>
                                <td @click="openDialog(item)">{{ item.req_date }}</td>
                                <td>
                                    <v-row no-gutters>
                                        <div
                                            style="color: white;"
                                            :class="
                                            item.response?.status === 2 ? 'completed'
                                            : item.response?.status == 1 ? 'answered'
                                            : item.response?.status == 0 ? 'rejected' : 'waiting'"
                                            @click="openDialog(item)"
                                        >
                                            {{ item.response?.status == 2 ? 'completed'
                                                : item.response?.status == 1 ? 'answered'
                                                : item.response?.status == 0 ? 'rejected': 'waiting' }}
                                        </div>
                                        <v-icon
                                            color="green"
                                            v-if="item.response?.status == 1"
                                            class="ml-1"
                                            @click="postCompleted(item.response.id)"
                                        >
                                            mdi-check
                                        </v-icon>
                                    </v-row>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card>

            <v-dialog
                v-model="dialog"
                transition="dialog-bottom-transition"
                max-width="50%"
            >
                <v-card
                    elevation="0"
                    class="pa-6"
                >
                <!-- item, material number, vendor -->
                    <v-row no-gutters>
                        <v-col cols="12" md="4" sm="4" xs="4">
                            <v-text-field
                                outlined
                                dense
                                label="item"
                                :value="request.item?.title"
                                readonly
                                class="mr-1"
                            />
                        </v-col>
                        <v-col cols="12" md="4" sm="4" xs="4">
                            <v-text-field
                                outlined
                                dense
                                label="material_number"
                                :value="request.item?.material_number"
                                readonly
                                class="mx-1"
                            />
                        </v-col>
                        <v-col cols="12" md="4" sm="4" xs="4">
                            <v-text-field
                                outlined
                                dense
                                label="vendor"
                                :value="request.item?.vendor"
                                readonly
                                class="ml-1"
                            />
                        </v-col>
                    </v-row>
                <!-- note, quantity, bin_location -->
                    <v-row no-gutters>
                        <v-col cols="12" md="4" sm="4" xs="4">
                            <v-text-field
                                outlined
                                dense
                                label="note"
                                :value="request.item?.note"
                                readonly
                                class="mr-1"
                            />
                        </v-col>
                        <v-col cols="12" md="4" sm="4" xs="4">
                            <v-text-field
                                outlined
                                dense
                                label="quantity"
                                :value="request.item?.quantity"
                                readonly
                                class="mx-1"
                            />
                        </v-col>
                        <v-col cols="12" md="4" sm="4" xs="4">
                            <v-text-field
                                outlined
                                dense
                                label="bin_location"
                                :value="request.item?.bin_location"
                                readonly
                                class="ml-1"
                            />
                        </v-col>
                    </v-row>
                <!-- images -->
                    <v-row no-gutters>
                        <v-col
                            cols="12"
                            md="2"
                            sm="2"
                            xs="2"
                            v-for="(img, i) in request.item?.image"
                            :key="i"
                        >
                            <v-img
                                height="100"
                                :src="`${url}${img.src}`"
                                class="ma-3"
                                style="border-radius: 5px;"
                            />
                        </v-col>
                    </v-row>
                <!-- res description, res status -->
                    <v-row no-gutters class="mt-5">
                        <v-col cols="12" md="10" sm="10" xs="10">
                            <v-text-field
                                v-if="request.response != null"
                                outlined
                                dense
                                label="response description"
                                :value="request.response?.description"
                                :readonly="request.response?.description"
                                class="mr-1"
                                hide-details
                            />

                            <v-text-field
                                v-if="request.response == null"
                                outlined
                                dense
                                label="response description"
                                v-model="descriptionModel"
                                class="mr-1"
                                hide-details
                            />
                        </v-col>
                        <v-col cols="12" md="2" sm="2" xs="2">

                            <v-text-field
                                v-if="request.response != null"
                                outlined
                                dense
                                label="status"
                                :value="
                                    request.response?.status == 2 ? 'completed'
                                    : request.response?.status == 1 ? 'not completed'
                                    : request.response?.status == 0 ? 'rejected'
                                    : ''"
                                readonly
                                class="ml-1"
                                hide-details
                            />

                            <v-combobox
                                v-if="request.response == null"
                                dense
                                outlined
                                hide-details
                                :items="response_status"
                                v-model="responseStatusModel"
                                label="status"
                                clearable
                                class="ml-1"
                            />
                        </v-col>
                    </v-row>

                    <v-row no-gutters class="mt-5">
                        <v-spacer/>
                        <v-btn
                            elevation="0"
                            color="#0BB923"
                            :disabled="request.response != null"
                            :style="!request.response ? 'color: white' : ''"
                            @click="postResponse(request.id)"
                        >
                            Save
                        </v-btn>
                    </v-row>
                </v-card>
            </v-dialog>
        </div>
      <div style="width: 100%; height: 100%; display: flex; justify-content: center;align-items: center">
        <v-img
            v-if="requests.length === 0 && !isLoading"
            src="@/assets/no-data.png"
            style="position: absolute;width: 50%"
        />
      </div>
      <loading-animation v-if="isLoading"/>
    </v-app>
</template>
    

<script>
import axios from 'axios';
import BASE_URL from '@/utils/url';
import Swal from 'sweetalert2';
import LoadingAnimation from "@/components/example/LoadingAnimation.vue";
export default {
  components: {LoadingAnimation},
    data: () => ({
        headers: ['id', 'item', 'count_in_stock', 'req_quantity', 'req_date', 'status'],
        status: ['answered', 'waiting'],
        response_status: ['accept', 'reject'],
        responseStatusModel: null,
        descriptionModel: null,
        statusModel: null,
        requests: [],
        request: {},
        dialog: false,
        isLoading: true,
        url: BASE_URL,
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
        this.getRequest()
    },
    methods: {
        async getRequest() {
            let status = this.statusModel == 'answered' ? true : this.statusModel == 'waiting' ? false : null
            const params = {
                st: status
            }
            await axios.get('/request/', { params: params })
            .then((res) => {
                this.requests = res.data.data
                this.isLoading = false
            })
            .catch((err) => {
                console.log(err)
            })
        },


        async openDialog(item) {
            this.request = item
            this.dialog = !this.dialog
        },

        async postResponse(request_id) {
            if (this.responseStatusModel == null) {
                this.Toast.fire({
                    icon:'error',
                    title: 'Status must be selected'
                })
                return
            }
            const params = {
                request_id: request_id,
                status: this.responseStatusModel == 'accept' ? 1 : this.responseStatusModel == 'reject' ? 0 : 0,
                description: this.descriptionModel
            }
            
            await axios.post('/response/', params)
            .then(() => {
                this.Toast.fire({
                    icon:'success',
                    title: 'Successfully answered'
                })
                this.dialog = !this.dialog
                this.getRequest()
                this.responseStatusModel = null
                this.descriptionModel = null
            })
            .catch((err) => {
                console.log(err)
                this.Toast.fire({
                    icon:'error',
                    title: 'Something went wrong'
                })
            })
        },

        async postCompleted(id) {
            await axios.patch(`/response/${id}/`, {
                status: 2
            }).
            then(() => {
                this.Toast.fire({
                    icon:'success',
                    title: 'Successfully completed'
                })
                this.getRequest()
            })
            .catch((err) => {
                console.log(err)
                this.Toast.fire({
                    icon:'error',
                    title: 'Something went wrong'
                })
            })
        }
    },
    computed: {
    },
    props: {
        
    }
}
</script>


<style scoped>

.answered {
    background-color: green;
    display: flex;
    justify-content: center;
    width: 75px;
    border-radius: 10px;
}
.waiting {
    background-color: orange;
    display: flex;
    justify-content: center;
    width: 60px;
    border-radius: 10px;
}
.rejected {
    background-color: red;
    display: flex;
    justify-content: center;
    width: 65px;
    border-radius: 10px;
}

.completed {
    background-color: #616161;
    display: flex;
    justify-content: center;
    width: 80px;
    border-radius: 10px;
}
.table-row{
    cursor: pointer;
}
</style>