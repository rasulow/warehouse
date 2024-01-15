<template>
    <v-app style="background-color: #F2F2F7;">
        <div style="
            margin: 20px;
            background-color: white;
            border-radius: 10px;
            padding: 15px"
        >
            <v-row no-gutters>
                <v-col 
                    cols="12" 
                    md="3" 
                    sm="6" 
                    xs="12"
                    v-for="(item, i) in dashboardCards"
                    :key="i"
                    class="pa-4"
                >
                    <v-card
                        width="100%"
                        :color="item.color"
                        class="dashboard-card pa-5"
                        elevation="0"
                        tile
                        
                    >
                        <v-row no-gutters>
                            <v-icon 
                                color="primary"
                                size="35"
                            >
                                {{ item.icon }}
                            </v-icon>
                        </v-row>
                        <v-row no-gutters>
                            <div style="color: black; font-size: 30px; font-weight: 500;">{{ item.count }}</div>
                        </v-row>
                        
                        <v-row no-gutters>
                            <div style="color: black; font-size: 20px; font-weight: 200;">{{ item.text }}</div>
                        </v-row>
                    </v-card>
                </v-col>
            </v-row>
            <div class="mt-10 pa-4">
                <apexchart type="bar" height="500" :options="BarChartOptions" :series="BarSeries"></apexchart>
            </div>
            <div class="mt-10 pa-4">
                <apexchart type="line" height="500" :options="LineChartOptions" :series="LineSeries"></apexchart>
            </div>
        </div>
    </v-app>
</template>

<script src="./DashboardPage.js"/>

<style scoped src="./DashboardPage.css"/>