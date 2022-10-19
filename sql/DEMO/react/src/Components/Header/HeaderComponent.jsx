import React, { useState } from "react";
import { Box } from "@material-ui/core";
import Navbar from "./Navbar";
import Sidenav from "./Sidenav";
import { Switch, Route } from "react-router-dom";
import Dashboard from "../BodyComponent/Dashboard/Dashboard";
import ServerComponent from "../BodyComponent/ServerComponent";
// import ServerComponent from "../BodyComponent/ServerComponent";
import Link from "../BodyComponent/Link";
import Notification from "../BodyComponent/Notification";
import Settings from "../BodyComponent/Settings";
import { useStyles } from "./HeaderStyles";
import User from "../BodyComponent/User/User";

export default function HeaderComponent() {
  const classes = useStyles();

  const [mobileOpen, setMobileOpen] = useState(false);
  const handleDrawerOpen = () => {
    setMobileOpen(!mobileOpen);
  };
  const handleDrawerClose = () => {
    setMobileOpen(false);
  };
  return (
    <div>
      <Navbar handleDrawerOpen={handleDrawerOpen} />
      <Sidenav
        mobileOpen={mobileOpen}
        handleDrawerOpen={handleDrawerOpen}
        handleDrawerClose={handleDrawerClose}
      />
      {/* // registerian our routes  */}
      <Box className={classes.wrapper}>
        <Switch>
          {/* <Route path='/' component={<Dashboard />} /> */}
          <Route exact path="/servers" render={() => <ServerComponent />} />
          <Route exact path="/link" render={() => <Link />} />
          <Route exact path="/user" render={() => <User />} />

          <Route exact path="/notification" render={() => <Notification />} />
          <Route exact path="/Settings" render={() => <Settings />} />
          <Route exact path="/" render={() => <Dashboard />} />
        </Switch>
      </Box>
    </div>
  );
}
