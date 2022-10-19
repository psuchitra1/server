import React from "react";
// import React, { useState } from "react";
import "./User.css";

// import {

// } from "@material-ui/icons";
import {
  Avatar,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TablePagination,
  TableRow,
  Box,
  Tabs,
  Typography,
  Tab,
  Button,
  Modal,
  TextField,
} from "@material-ui/core";
import PropTypes from "prop-types";
import { useStyles } from "../../Header/HeaderStyles";
import image from "../../Header/Navtabs/adduser.png";
// import { Height } from "@material-ui/icons";
// import ImageButton from "react-image-button";

const columns = [
  { id: "code", label: "ID", minWidth: 170, align: "center" },
  { id: "name", label: "User Name", minWidth: 100, align: "center" },
  {
    id: "population",
    label: "Role",
    minWidth: 170,
    align: "center",
    format: (value) => value.toLocaleString("en-US"),
  },
  {
    id: "size",
    label: "email",
    minWidth: 170,
    align: "center",
    format: (value) => value.toLocaleString("en-US"),
  },
  {
    id: "density",
    label: "Team ID",
    minWidth: 170,
    align: "center",
    format: (value) => value.toFixed(2),
  },
];

function createData(name, code, population, size, density) {
  // const density = population / size;
  return { name, code, population, size, density };
}

const rows = [
  createData("Arun S K", "01", "Infra Admin", "arunsk@gmail.com", "T1"),
  createData("Sachin S K", "02", "USER", "sachinsk@gmail.com", "T1"),
  createData("Komal", "03", "USER", "komal@gmail.com", "T1"),
  createData("Vibha", "04", "USER", "vibha@gmail.com", "T1"),
  createData("Mani", "05", "USER", "mani@gmail.com", "T1"),
  createData("Aparna", "06", "USER", "aparna@gmail.com", "T1"),
  createData("anjana", "07", "USER", "anjana@gmail.com", "T1"),
  createData("umar", "08", "USER", "umar@gmail.com", "T1"),
  createData("aswin", "09", "USER", "aswin@gmail.com", "T1"),
  createData("arun", "10", "USER", "arun@gmail.com", "T1"),
];

const rows1 = [
  createData("Arun S K", "01", "Infra Admin", "arunsk@gmail.com", "T1"),
];

const rows2 = [
  createData("Sachin S K", "02", "USER", "sachinsk@gmail.com", "T1"),
  createData("Komal", "03", "USER", "komal@gmail.com", "T1"),
  createData("Vibha", "04", "USER", "vibha@gmail.com", "T1"),
  createData("Mani", "05", "USER", "mani@gmail.com", "T1"),
  createData("Aparna", "06", "USER", "aparna@gmail.com", "T1"),
  createData("anjana", "07", "USER", "anjana@gmail.com", "T1"),
  createData("umar", "08", "USER", "umar@gmail.com", "T1"),
  createData("aswin", "09", "USER", "aswin@gmail.com", "T1"),
  createData("arun", "10", "USER", "arun@gmail.com", "T1"),
];

export default function User() {
  const classes = useStyles();
  // const [setAnchorEl] = useState(null);
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
      <div
        role="tabpanel"
        hidden={value !== index}
        id={`simple-tabpanel-${index}`}
        aria-labelledby={`simple-tab-${index}`}
        {...other}
      >
        {value === index && (
          <Box sx={{ p: 3 }}>
            <Typography>{children}</Typography>
          </Box>
        )}
      </div>
    );
  }

  TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.number.isRequired,
    value: PropTypes.number.isRequired,
  };

  function a11yProps(index) {
    return {
      id: `simple-tab-${index}`,
      "aria-controls": `simple-tabpanel-${index}`,
    };
  }

  //----------------------------- Add User Tab -----------------------------
  const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 600,
    height: 400,
    bgcolor: "#344675",
    boxShadow: 24,
    pt: 2,
    px: 4,
    pb: 3,
  };

  const [open, setOpen] = React.useState(false);
  const handleOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  //------------------------------ / Add User Tab --------------------------

  return (
    <>
      <Paper sx={{ width: "100%", overflow: "hidden" }}>
        {/* <div>
          <Button onClick={handleOpen}>Open modal</Button>
          <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="parent-modal-title"
            aria-describedby="parent-modal-description"
          >
            <Box sx={{ ...style, width: 400 }}>
              <h2 id="parent-modal-title">Text in a modal</h2>
              <p id="parent-modal-description">
                Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
              </p>
            </Box>
          </Modal>
        </div> */}
        <div style={{ paddingLeft: "93%" }}>
          <br />
          <Button
            onClick={handleOpen}
            aria-controls="simple-menu"
            aria-haspopup="true"
            startIcon={
              <Avatar src={image} className={classes.addUser}></Avatar>
            }
          ></Button>
          <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="parent-modal-title"
            aria-describedby="parent-modal-description"
          >
            <Box sx={{ ...style, width: 400 }}>
              <h2 id="parent-modal-title">Text in a modal</h2>
              <p id="parent-modal-description">
                Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
                <div>
                  <form className={classes.root} noValidate autoComplete="off">
                    <div>
                      <TextField
                        error
                        id="standard-error"
                        label="Error"
                        defaultValue="Hello World"
                      />
                      <TextField
                        error
                        id="standard-error-helper-text"
                        label="Error"
                        defaultValue="Hello World"
                        helperText="Incorrect entry."
                      />
                    </div>
                    <div>
                      <TextField
                        error
                        id="filled-error"
                        label="Error"
                        defaultValue="Hello World"
                        variant="filled"
                      />
                      <TextField
                        error
                        id="filled-error-helper-text"
                        label="Error"
                        defaultValue="Hello World"
                        helperText="Incorrect entry."
                        variant="filled"
                      />
                    </div>
                    <div>
                      <TextField
                        error
                        id="outlined-error"
                        label="Error"
                        defaultValue="Hello World"
                        variant="outlined"
                      />
                      <TextField
                        error
                        id="outlined-error-helper-text"
                        label="Error"
                        defaultValue="Hello World"
                        helperText="Incorrect entry."
                        variant="outlined"
                      />
                    </div>
                  </form>
                </div>
              </p>
            </Box>
          </Modal>
        </div>
        <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
          <Tabs
            value={value}
            onChange={handleChange}
            aria-label="basic tabs example"
          >
            <Tab label="ALL" {...a11yProps(0)} />
            <Tab label="Infra User" {...a11yProps(1)} />
            <Tab label="User" {...a11yProps(2)} />
          </Tabs>
        </Box>
        <TabPanel value={value} index={0}>
          <TableContainer sx={{ maxHeight: 440 }}>
            <Table stickyHeader aria-label="sticky table">
              <TableHead>
                <TableRow>
                  {columns.map((column) => (
                    <TableCell
                      key={column.id}
                      align={column.align}
                      style={{ minWidth: column.minWidth }}
                    >
                      {column.label}
                    </TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {rows
                  .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  .map((row) => {
                    return (
                      <TableRow
                        hover
                        role="checkbox"
                        tabIndex={-1}
                        key={row.code}
                      >
                        {columns.map((column) => {
                          const value = row[column.id];
                          return (
                            <TableCell key={column.id} align={column.align}>
                              {column.format && typeof value === "number"
                                ? column.format(value)
                                : value}
                            </TableCell>
                          );
                        })}
                      </TableRow>
                    );
                  })}
              </TableBody>
            </Table>
          </TableContainer>
          <TablePagination
            rowsPerPageOptions={[10, 25, 100]}
            component="div"
            count={rows.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </TabPanel>
        <TabPanel value={value} index={1}>
          <TableContainer sx={{ maxHeight: 440 }}>
            <Table stickyHeader aria-label="sticky table">
              <TableHead>
                <TableRow>
                  {columns.map((column) => (
                    <TableCell
                      key={column.id}
                      align={column.align}
                      style={{ minWidth: column.minWidth }}
                    >
                      {column.label}
                    </TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {rows1
                  .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  .map((row) => {
                    return (
                      <TableRow
                        hover
                        role="checkbox"
                        tabIndex={-1}
                        key={row.code}
                      >
                        {columns.map((column) => {
                          const value = row[column.id];
                          return (
                            <TableCell key={column.id} align={column.align}>
                              {column.format && typeof value === "number"
                                ? column.format(value)
                                : value}
                            </TableCell>
                          );
                        })}
                      </TableRow>
                    );
                  })}
              </TableBody>
            </Table>
          </TableContainer>
          <TablePagination
            rowsPerPageOptions={[10, 25, 100]}
            component="div"
            count={rows1.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </TabPanel>
        <TabPanel value={value} index={2}>
          <TableContainer sx={{ maxHeight: 440 }}>
            <Table stickyHeader aria-label="sticky table">
              <TableHead>
                <TableRow>
                  {columns.map((column) => (
                    <TableCell
                      key={column.id}
                      align={column.align}
                      style={{ minWidth: column.minWidth }}
                    >
                      {column.label}
                    </TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {rows2
                  .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  .map((row) => {
                    return (
                      <TableRow
                        hover
                        role="checkbox"
                        tabIndex={-1}
                        key={row.code}
                      >
                        {columns.map((column) => {
                          const value = row[column.id];
                          return (
                            <TableCell key={column.id} align={column.align}>
                              {column.format && typeof value === "number"
                                ? column.format(value)
                                : value}
                            </TableCell>
                          );
                        })}
                      </TableRow>
                    );
                  })}
              </TableBody>
            </Table>
          </TableContainer>
          <TablePagination
            rowsPerPageOptions={[10, 25, 100]}
            component="div"
            count={rows2.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </TabPanel>
      </Paper>
    </>
  );
}
