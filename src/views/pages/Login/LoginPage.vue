<template>
    <v-app style="background-color: #F2F2F7;">
        <v-container>
            <v-row class="d-flex justify-center align-center" style="margin-top: 200px;">
                <v-col cols="12" sm="12" class="d-flex justify-center align-center">
                    <v-card
                        width="500"
                        height="400"
                        style="padding: 40px;"
                        elevation="0"
                        tile
                    >
                        <v-col>
                            <v-row no-gutters justify="start">
                                <v-card-title class="pa-0 mb-8 login-text">Ulgama girmek</v-card-title>
                            </v-row>
                            <v-row no-gutters justify="start">
                                <v-text-field
                                    label="Ulanyjy ady"
                                    v-model="username"
                                    outlined
                                    :rules="usernameRules"
                                />
                            </v-row>
                            <v-row no-gutters justify="start">
                                <v-text-field
                                    v-model="password"
                                    :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                    :type="show1 ? 'text' : 'password'"
                                    label="Açar sözi"
                                    @click:append="show1 = !show1"
                                    outlined
                                    tile
                                    :rules="passwordRules"
                                />
                            </v-row>
                            <v-btn
                                elevation="0"
                                width="100%"
                                height="50"
                                style="font-size: larger;font-weight: 200;color: white;"
                                color="#0BB923"
                                tile
                                @click="login"
                            >
                                Ulgama girmek
                            </v-btn>
                        </v-col>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<script src="./LoginPage.js">

</script>


<style scoped src="./LoginPage.css">

</style>
