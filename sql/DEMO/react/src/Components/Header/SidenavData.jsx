import React from "react";
import {
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Button,
} from "@material-ui/core";

import DashboardIcon from "@material-ui/icons/Dashboard";
// import BookIcon from "@material-ui/icons/Book";
import PostAddIcon from "@material-ui/icons/PostAdd";
// import NotificationsActiveIcon from "@material-ui/icons/NotificationsActive";
// import ExitToAppIcon from "@material-ui/icons/ExitToApp";
import StorageIcon from "@material-ui/icons/Storage";
import People from "@material-ui/icons/People";
import Settings from "@material-ui/icons/Settings";
import { NavLink } from "react-router-dom";
import { useStyles } from "./HeaderStyles";
// import StorageIcon from "@mui/icons-material/Storage";

export default function SidenavData({ handleDrawerClose }) {
  const classes = useStyles();
  const listItemData = [
    { label: "Dashobard", link: "/", icon: <DashboardIcon /> },
    { label: "Servers", link: "/servers", icon: <StorageIcon /> },
    { label: "Approvals", link: "/Approvals", icon: <PostAddIcon /> },
    { label: "Users", link: "/user", icon: <People /> },
    { label: "Settings", link: "/settings", icon: <Settings /> },
    // {
    //   label: "Notification",
    //   link: "/notification",
    //   icon: <NotificationsActiveIcon />,
    // },
    // { label: "Logout", link: "/logout", icon: <ExitToAppIcon /> },
  ];
  return (
    <List>
      {listItemData.map((item, i) => (
        <Button
          size="small"
          className={classes.navButton}
          onClick={() => handleDrawerClose()}
          key={i}
        >
          <ListItem
            exact
            component={NavLink}
            to={item.link}
            className={classes.navlinks}
            activeClassName={classes.activeNavlinks}
          >
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText>{item.label}</ListItemText>
          </ListItem>
        </Button>
      ))}
    </List>
  );
}
