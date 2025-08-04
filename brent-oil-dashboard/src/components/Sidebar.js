import React from 'react';
import { Drawer, List, ListItem, ListItemText, ListItemIcon } from '@mui/material';
import DashboardIcon from '@mui/icons-material/Dashboard';
import InsightsIcon from '@mui/icons-material/Insights';
import { Typography, Box } from '@mui/material';
import { Divider } from '@mui/material';

const drawerWidth = 240;

const Sidebar = () => (
  <Drawer
    variant="permanent"
    anchor="left"
    sx={{
      width: drawerWidth,
      flexShrink: 0,
      '& .MuiDrawer-paper': {
        width: drawerWidth,
        boxSizing: 'border-box',
        backgroundColor: '#0f172a', // Dark slate background
        color: 'white',
      },
    }}
  >
    <Box sx={{ p: 2, textAlign: 'center' }}>
        <Typography variant="h6" sx={{ fontWeight: 'bold', color: '#38bdf8' }}>
            Oil Insights 📈
        </Typography>
    </Box>
    <List>
      <ListItem button sx={{ '&:hover': { backgroundColor: '#1e293b' } }}>
        <ListItemIcon>
          <DashboardIcon sx={{ color: 'white' }} />
        </ListItemIcon>
        <ListItemText primary="Dashboard" />
      </ListItem>
      <Divider sx={{ backgroundColor: 'rgba(255,255,255,0.2)', my: 2 }} />
      <ListItem button sx={{ '&:hover': { backgroundColor: '#1e293b' } }}>
        <ListItemIcon>
          <InsightsIcon sx={{ color: 'white' }} />
        </ListItemIcon>
        <ListItemText primary="Analytics" />
      </ListItem>
      <Divider sx={{ backgroundColor: 'rgba(255,255,255,0.2)', my: 2 }} />
    </List>
  </Drawer>
);

export default Sidebar;
