// import React from 'react';
// import { AppBar, Toolbar, Typography } from '@mui/material';

// const Topbar = () => (
//   <AppBar position="static" color="primary">
//     <Toolbar>
//       <Typography variant="h6">Oil Price Dashboard</Typography>
//     </Toolbar>
//   </AppBar>
// );

// export default Topbar;

import React from 'react';
import { AppBar, Toolbar, Typography, IconButton, Avatar } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import { Box } from '@mui/material';
import NotificationsIcon from '@mui/icons-material/Notifications';

const Topbar = ({ title }) => (
  <AppBar
    position="static"
    sx={{
      zIndex: (theme) => theme.zIndex.drawer + 1,
      backgroundColor: '#1e293b', // Midnight blue
      boxShadow: '0 2px 10px rgba(0, 0, 0, 0.3)',
    }}
  >
    <Toolbar sx={{ display: 'flex', justifyContent: 'space-between', px: 3 }}>
      <Typography variant="h6" sx={{ color: '#38bdf8', fontWeight: 'bold' }}>
        {title}
      </Typography>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
        <IconButton size="large" sx={{ color: 'white' }}>
          <NotificationsIcon />
        </IconButton>
        <Avatar alt="Estifanose" src="/avatar.png" sx={{ bgcolor: '#38bdf8', color: '#0f172a' }} />
      </Box>
    </Toolbar>
  </AppBar>
);

export default Topbar;