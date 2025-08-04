import React from 'react';
import { Box, Grid, Paper, Typography } from '@mui/material';
import Sidebar from '../components/Sidebar';
import Topbar from '../components/Topbar';
import Chart from '../components/Chart';

const drawerWidth = 240;

const Dashboard = () => (
  <Box sx={{ display: 'flex' }}>
    <Sidebar />
    <Box component="main" sx={{ flexGrow: 1, p: 3, marginLeft: `0px` }}>
      <Topbar title="Oil Price Dashboard" />
      <Typography variant="h4" gutterBottom>Oil Price Trends</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Paper elevation={3}>
            <Chart />
          </Paper>
        </Grid>
      </Grid>
    </Box>
  </Box>
);

export default Dashboard;
