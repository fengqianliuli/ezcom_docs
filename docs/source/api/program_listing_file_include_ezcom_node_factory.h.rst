
.. _program_listing_file_include_ezcom_node_factory.h:

Program Listing for File node_factory.h
=======================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_node_factory.h>` (``include/ezcom/node_factory.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   #include <memory>
   #include <vector>
   
   #include "client.h"
   #include "publisher.h"
   #include "server.h"
   #include "subscriber.h"
   
   namespace holosar {
   namespace ezcom {
   
   class NodeFactory {
    public:
     static std::unique_ptr<Client> CreateClient(
         const TransportType& transport_type);
     static std::unique_ptr<Server> CreateServer(
         const TransportType& transport_type);
     // TODO: inproc
     //   static void CreateZmqInprocNodes(int node_num, std::unique_ptr<Server>*
     //   server,
     //       std::vector<std::unique_ptr<Client>*>& clients);
   
     static std::unique_ptr<Publisher> CreatePublisher(
         const TransportType& transport_type);
     static std::unique_ptr<Subscriber> CreateSubscriber(
         const TransportType& transport_type);
     // TODO: inproc
     //   static void CreateZmqInprocNodes(int node_num, std::unique_ptr<Pub>* pub,
     //       std::vector<std::unique_ptr<Sub>*>& subs);
    private:
     static std::unique_ptr<Node> CreateNode(const NodeType& node_type,
                                             const CommMode& comm_mode,
                                             const TransportType& transport_type);
     static std::vector<std::unique_ptr<Node>> CreateZmqInprocNode(
         const CommMode& comm_mode, int node_num);
   };
   
   }  // namespace ezcom
   }  // namespace holosar
