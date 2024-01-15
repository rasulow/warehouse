<template>
    <v-card
        elevation="0"
        color="white"
        width="100%"
        style="border-radius: 10px; padding: 15px"
    >
        <v-row no-gutters>
            <v-col cols="12" md="2" sm="2">
              <v-combobox
                  v-if="showType"
                  dense
                  outlined
                  hide-details
                  :items="types"
                  v-model="typeModel"
                  label="is_deleted"
                  @change="$emit('change-type', typeModel)"
                  clearable
              />
            </v-col>
            <v-spacer/>
            <v-btn
                elevation="0"
                style="color: #0BB923; border: 1px solid #0BB923; background-color: transparent"
                @click="$emit('open-dialog')"
                tile
            >
                <v-icon color="#0BB923"> {{ icon }} </v-icon>
                +
            </v-btn>
        </v-row>
    </v-card>
</template>

<script>
    export default {
        data: () => ({
          types: ['True', 'False'],
          typeModel: null
        }),
        props: {
            icon: {
                type: String,
                required: true,
            },
            showType: {
              type: Boolean,
              default: false
            }
        },
        methods: {
            emitOpenNavDrawer() {
                this.$emit('open-nav-drawer');
            }
        }
    }
</script>
    