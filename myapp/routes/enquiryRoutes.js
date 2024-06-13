const express = require('express');
const router = express.Router();
const Enquiry = require('../models/Enquiry');

// Add Enquiry Route
router.post('/enquiry', async (req, res) => {
    const { email, company_name, country_restrictions, phone_no, delivery_address, materials } = req.body;
    try {
        const newEnquiry = new Enquiry({
            email,
            company_name,
            country_restrictions,
            phone_no,
            delivery_address,
            materials,
        });
        await newEnquiry.save();
        res.status(201).json({ message: 'Enquiry added successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error adding enquiry', error });
    }
});

module.exports = router;
