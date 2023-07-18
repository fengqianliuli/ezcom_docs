
.. _program_listing_file_include_ezcom_exception.h:

Program Listing for File exception.h
====================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_exception.h>` (``include/ezcom/exception.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   #include <stdexcept>
   
   namespace holosar {
   namespace ezcom {
   
   class Exception : public std::runtime_error {
    public:
     Exception(const std::string& msg) : std::runtime_error(msg) {}
   };
   
   class InvalidParamException : public Exception {
    public:
     InvalidParamException(const std::string& msg) : Exception(msg) {}
   };
   
   class ResourceException : public Exception {
    public:
     ResourceException(const std::string& msg) : Exception(msg) {}
   };
   
   class AlreadyDoneException : public Exception {
    public:
     AlreadyDoneException(const std::string& msg) : Exception(msg) {}
   };
   
   }  // namespace ezcom
   }  // namespace holosar
