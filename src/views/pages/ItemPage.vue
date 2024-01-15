<template>
    <v-app style="background-color: #F2F2F7;">
        <div style="margin: 20px"

        >
            <v-card
                elevation="0"
                color="white"
                width="100%"
                style="border-radius: 10px; padding: 15px"
                v-if="!isLoading"
            >
                <v-row no-gutters>
                    <v-col cols="12" sm="2" md="2" xs="2">
                        <v-combobox
                            dense
                            outlined
                            hide-details
                            :items="category"
                            item-text="name"
                            v-model="categoryModel"
                            label="Kategoriýa"
                            @change="getItem()"
                            clearable
                            class="mr-1"
                        />
                    </v-col>
                    <v-col cols="12" sm="2" md="2" xs="2">
                        <v-combobox
                            dense
                            outlined
                            hide-details
                            :items="retrievedList"
                            v-model="retrievedModel"
                            label="ýagdaýy"
                            @change="getItem()"
                            clearable
                            class="ml-1"
                        />
                    </v-col>
                    <v-spacer/>
                    <v-col cols="12" sm="4" md="4" xs="4">
                        <v-text-field
                            outlined
                            dense
                            label="Gözleg..."
                            placeholder="title, material_number, vendor"
                            hide-details
                            v-model="search"
                            @input="getItem()"
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
                v-if="items.length > 0"
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
                                v-for="(item, i) in items"
                                :key="i"
                                :style="i % 2 === 0 ? 'background-color: #F2F2F7': ''"
                                class="table-row"
                            >
                                <td @click="openDialog(item)">{{ item.id }}</td>
                                <td @click="openDialog(item)">{{ item.category.name }}</td>
                                <td @click="openDialog(item)">{{ item.title }}</td>
                                <td @click="openDialog(item)">{{ item.quantity }}</td>
                                <td @click="openDialog(item)">{{ item.bin_location }}</td>
                                <td @click="openDialog(item)">
                                    <div :class="item.is_retrieved ? 'is-retrieved-box-style-passive' : 'is-retrieved-box-style-active'">
                                        {{ item.is_retrieved ? 'old' : 'new' }}
                                    </div>
                                </td>
                                <td style="width: 75px">
                                    
                                    <v-btn icon style="border: 1px solid #AEAEAE" class="ml-1" @click="deleteItem(item.id)">
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
                max-width="50%"
            >
                <v-card 
                    elevation="0"
                    class="pa-6"
                >
                <div style="font-size: 30px;margin-bottom: 15px;">Full information</div>
                <!-- title material_number -->
                    <v-row no-gutters>
                        <v-col cols="12" sm="6" md="6" xs="6">
                            <v-text-field
                                outlined
                                dense
                                label="title"
                                :value="item.title"
                                readonly
                                class="mr-1"
                            />
                        </v-col>
                        <v-col cols="12" sm="6" md="6" xs="6">
                            <v-text-field
                                outlined
                                dense
                                label="material number"
                                :value="item.material_number"
                                readonly
                                class="ml-1"
                            />
                        </v-col>
                    </v-row>
                <!-- vendor quantity bin_location -->
                    <v-row no-gutters>
                        <v-col cols="12" sm="3" md="3" xs="3">
                            <v-text-field
                                outlined
                                dense
                                label="vendor"
                                :value="item.vendor"
                                readonly
                                class="mr-1"
                            />
                        </v-col>
                        <v-col cols="12" sm="3" md="3" xs="3">
                            <v-text-field
                                outlined
                                dense
                                label="quantity"
                                :value="item.quantity"
                                readonly
                                class="mx-1"
                            />
                        </v-col>
                        <v-col cols="12" sm="3" md="3" xs="3">
                            <v-text-field
                                outlined
                                dense
                                label="bin_location"
                                :value="item.bin_location"
                                readonly
                                class="mx-1"
                            />
                        </v-col><v-col cols="12" sm="3" md="3" xs="3">
                            <v-text-field
                                outlined
                                dense
                                label="price"
                                :value="item.price"
                                readonly
                                class="ml-1"
                            />
                        </v-col>
                    </v-row>
                <!-- category note -->
                    <v-row no-gutters>
                        <v-col cols="12" sm="6" md="6" xs="6">
                            <v-text-field
                                outlined
                                dense
                                label="note"
                                :value="item.note"
                                readonly
                                class="mr-1"
                                hide-details
                            />
                        </v-col>
                        <v-col cols="12" sm="6" md="6" xs="6">
                            <v-text-field
                                outlined
                                dense
                                label="category"
                                :value="item.category?.name"
                                readonly
                                class="ml-1"
                                hide-details
                            />
                        </v-col>
                    </v-row>
                <!-- images -->
                    <v-row no-gutters class="mt-5">
                        <v-col
                            cols="12"
                            md="2"
                            sm="2"
                            xs="2"
                            v-for="(img, i) in item.image"
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
                </v-card>
            </v-dialog>

        </div>
      <div style="width: 100%; height: 100%; display: flex; justify-content: center;align-items: center">
        <v-img
            v-if="items.length === 0 && !isLoading"
            src="@/assets/no-data.png"
            style="position: absolute;width: 50%"
        />
      </div>
      <loading-animation v-if="isLoading"/>
    </v-app>
</template>

<script>
import BASE_URL from '@/utils/url';
import Swal from 'sweetalert2';
import axios from 'axios';
import LoadingAnimation from "@/components/example/LoadingAnimation.vue";
export default {
    data: () => ({
        search: null,
        dialog: false,
        headers: ['id', 'Kategoriýasy', 'ady', 'sany', 'ýerleşýän ýeri', 'ýagdaýy', 'action'],
        category: [],
        categoryModel: null,
        retrievedList: ['old', 'new'],
        retrievedModel: null,
        items: [],
        item: {},
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
        this.getCategory(),
        this.getItem()
    },
    methods: {
        openDialog(item) {
            this.item = item
            this.dialog = !this.dialog
        },

        async getCategory() {
            await axios.get('/category/')
            .then((res) => {
                this.category = res.data.data
            })
            .catch((err) => {
                console.log(err)
            })
        },

        async getItem() {
            console.log()
            let status = 
                this.retrievedModel === 'old' ? true :
                this.retrievedModel === 'new' ? false :
                null

            const params = {
                is_retrieved: status,
                category_id: this.categoryModel?.id,
                q: this.search
            }
            await axios.get('/item/', { params: params })
            .then((res) => {
                this.items = res.data.data
                this.isLoading = false
            })
            .catch((err) => {
                console.log(err)
            })
        },

        deleteItem(id) {
            Swal.fire({
                title: 'Hakykatdanam pozmak isleýärsiňizmi?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#7FBA5E',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Hawa, pozmaly!',
                cancelButtonText: 'Ýok!'
            })
            .then((res) => {
                if(res.isConfirmed) {
                    axios.delete(`/item/${id}/`)
                    .then(() => {
                        this.Toast.fire({
                            icon:'success',
                            title: 'Üstünlikli pozuldy'
                        })
                        this.getItem()
                    })
                    .catch((err) => {
                        console.log(err)
                        this.Toast.fire({
                            icon:'error',
                            title: 'Ýalňyşlyk ýüze çykdy!'
                        })
                    })
                }
            })
        }
    },
  components: {
      LoadingAnimation
  }
}
</script>


<style scoped>
.is-retrieved-box-style-active{
    background-color: green;
    max-width: 50px;
    min-height: 20px;
    display: flex;
    justify-content: center;
    border-radius: 10px;
    color: white;
}

.is-retrieved-box-style-passive {
    background-color: red;
    max-width: 50px;
    min-height: 20px;
    display: flex;
    justify-content: center;
    border-radius: 10px;
    color: white;
}

.table-row {
    cursor: pointer;
}
</style>